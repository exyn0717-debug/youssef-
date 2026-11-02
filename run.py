"""Run Method. Use --dev for local HTTP; production requires HTTPS."""
import os, argparse
from pathlib import Path
root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--dev',action='store_true',help='Local development only: HTTP cookies and localhost binding')
parser.add_argument('--host',default=None)
parser.add_argument('--port',type=int,default=int(os.environ.get('PORT','8000')))
args=parser.parse_args()
if args.dev:
    os.environ.setdefault('METHOD_ENV','development')
    os.environ.setdefault('METHOD_COOKIE_SECURE','0')
    os.environ.setdefault('METHOD_COOKIE_SAMESITE','strict')
import uvicorn
uvicorn.run('app.main:app',host=args.host or ('127.0.0.1' if args.dev else '0.0.0.0'),port=args.port,workers=1,proxy_headers=True,forwarded_allow_ips=os.environ.get('METHOD_TRUSTED_PROXIES','127.0.0.1'),server_header=False,log_level='info')
