import json,math
from .common import number,integer,identifier,unique_ids
import threading,contextlib
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.request import Request,build_opener,HTTPRedirectHandler
from urllib.parse import urlsplit
class StripCrossOrigin(HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  new=super().redirect_request(req,fp,code,msg,headers,newurl)
  a=urlsplit(req.full_url);b=urlsplit(newurl)
  if (a.scheme,a.hostname,a.port)!=(b.scheme,b.hostname,b.port):
   for key in list(new.headers):
    if key.lower()in ['authorization','cookie','x-api-key']:del new.headers[key]
  return new
@contextlib.contextmanager
def local_server(handler):
 server=ThreadingHTTPServer(('127.0.0.1',0),handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
 try:yield server
 finally:server.shutdown();server.server_close();thread.join(timeout=2)
def run(d):
 observed=[]
 class Receiver(BaseHTTPRequestHandler):
  def log_message(self,*a):pass
  def do_GET(self):
   observed.append({k.lower():v for k,v in self.headers.items()if k.lower()in ['authorization','cookie','x-api-key']});self.send_response(200);self.end_headers();self.wfile.write(b'ok')
 with local_server(Receiver)as destination:
  url='http://127.0.0.1:'+str(destination.server_port)+'/target'
  class Redirect(BaseHTTPRequestHandler):
   def log_message(self,*a):pass
   def do_GET(self):self.send_response(302);self.send_header('Location',url);self.end_headers()
  with local_server(Redirect)as origin:
   start='http://127.0.0.1:'+str(origin.server_port)+'/source';out={}
   for label,opener in [('stdlib',build_opener()),('strip_cross_origin',build_opener(StripCrossOrigin()))]:
    req=Request(start,headers={'Authorization':'Bearer SYNTHETIC_CANARY','Cookie':'synthetic=1','X-Api-Key':'SYNTHETIC_KEY'})
    with opener.open(req,timeout=3)as response:response.read(20)
    out[label]=dict(forwarded_header_names=sorted(observed[-1]),cross_origin=True)
 return dict(experiments=out,network_scope='two_localhost_servers_different_ports',uses_real_credentials=False)
