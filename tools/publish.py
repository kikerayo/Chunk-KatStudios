"""Publish a complete public Chunk build and atomically advance the stable manifest."""
import base64,hashlib,json,os,subprocess,sys,urllib.request,urllib.error,zipfile
from pathlib import Path
REPO='kikerayo/Chunk-KatStudios'
def api(method,path,data=None,content_type='application/json'):
 token=os.environ.get('GITHUB_TOKEN')
 if not token:
  p=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',text=True,capture_output=True,env=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='Never'),timeout=15)
  c=dict(line.split('=',1) for line in p.stdout.splitlines() if '=' in line);token=c.get('password')
 if not token:raise RuntimeError('Inicia sesión en GitHub mediante Git o GITHUB_TOKEN.')
 payload=json.dumps(data).encode() if isinstance(data,dict) else data
 req=urllib.request.Request(path if path.startswith('https://') else 'https://api.github.com'+path,data=payload,method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','User-Agent':'KatStudios-Chunk-Publisher','Content-Type':content_type})
 with urllib.request.urlopen(req,timeout=240) as r:return json.load(r)
def put(path,content):
 body={'message':'Publish '+path,'content':base64.b64encode(content).decode(),'branch':'main'}
 try:body['sha']=api('GET',f'/repos/{REPO}/contents/{path}')['sha']
 except urllib.error.HTTPError as e:
  if e.code!=404:raise
 return api('PUT',f'/repos/{REPO}/contents/{path}',body)
def publish(package):
 package=Path(package)
 with zipfile.ZipFile(package) as z:
  assert z.testzip() is None
  names=z.namelist()
  if any('/mundos/' in n or '/personalizacion/' in n or n.startswith('Chunk_Privada/') for n in names):raise ValueError('No publiques partidas ni edición privada')
  meta=json.loads(z.read('Chunk_Publica/chunk-release.json'))
  assert meta['game_id']=='chunk' and meta['studio']=='KatStudios'
 version=meta['version'];build=int(meta['build']);tag=f'v{version}-build{build}';name='Chunk-Windows-x64.zip'
 # A release asset is immutable; a failed run can resume before manifest publication.
 try:release=api('GET',f'/repos/{REPO}/releases/tags/{tag}')
 except urllib.error.HTTPError as e:
  if e.code!=404:raise
  release=api('POST',f'/repos/{REPO}/releases',{'tag_name':tag,'target_commitish':'main','name':f'Chunk {version} · KatStudios · build {build}','body':'Actualizaciones automáticas desde GitHub y marca KatStudios. Conserva mundos, configuración, personalización y mods. Consulta README y docs/KatLauncher.md.','draft':False,'prerelease':False,'make_latest':'true'})
 assets=api('GET',f'/repos/{REPO}/releases/{release["id"]}/assets')
 asset=next((a for a in assets if a['name']==name),None)
 digest=hashlib.file_digest(package.open('rb'),'sha256').hexdigest()
 if asset:
  if asset.get('digest')!='sha256:'+digest:raise ValueError('La release ya contiene un paquete diferente; aumenta BUILD')
 else:
  print('Subiendo paquete público:',round(package.stat().st_size/1024**2,1),'MiB',flush=True)
  asset=api('POST',release['upload_url'].split('{')[0]+'?name='+name,package.read_bytes(),'application/zip')
 if asset['size']!=package.stat().st_size or asset.get('digest') not in (None,'sha256:'+digest):raise ValueError('GitHub no confirma la integridad del asset')
 manifest={'schema_version':1,'game_id':'chunk','studio':'KatStudios','version':version,'build':build,'channel':'stable','release_url':release['html_url'],'platforms':{'windows-x64':{'url':asset['browser_download_url'],'sha256':digest,'size':asset['size'],'archive_root':'Chunk_Publica','executable':'Chunk_Publica.exe'}}}
 put('updates/stable.json',(json.dumps(manifest,indent=2)+'\n').encode())
 print(json.dumps({'repository':'https://github.com/'+REPO,'manifest':'https://raw.githubusercontent.com/'+REPO+'/main/updates/stable.json','release':release['html_url'],'sha256':digest}),flush=True)
 return manifest
if __name__=='__main__':publish(sys.argv[1])
