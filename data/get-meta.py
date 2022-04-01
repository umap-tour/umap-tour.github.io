from glob import glob
import json
from natsort import natsorted
import sys
import re
pattern = re.compile('epoch(\d+)/arch(\d+)')

folder = sys.argv[1] if len(sys.argv)>=2 else 'umap-4D'
fn_out = sys.argv[2] if len(sys.argv)>=3 else 'meta.json'
if not fn_out.endswith('json'):
    fn_out += '.json'
res = {}
res['epoch_arch_to_dir'] = {}
for fn in natsorted(glob(f'{folder}/epoch*/arch*/')):
    print(fn)
    epoch, arch = pattern.findall(fn)[0]
    epoch, arch = int(epoch), int(arch)
    res['epoch_arch_to_dir'][f'{epoch},{arch}'] = fn

print(res)

with open(fn_out, 'w') as f:
    json.dump(res, f, indent=2)