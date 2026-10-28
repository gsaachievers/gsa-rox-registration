# Run after installing qrcode[pil]: python -m pip install 'qrcode[pil]'
# Usage: python make_qr.py https://YOUR-USERNAME.github.io/gsa-rox-registration/
import sys, qrcode
if len(sys.argv)!=2 or not sys.argv[1].startswith('https://'):
    raise SystemExit('Usage: python make_qr.py https://YOUR-LIVE-GITHUB-PAGES-URL/')
qrcode.make(sys.argv[1]).save('gsa_rox_registration_qr.png')
print('Saved gsa_rox_registration_qr.png')
