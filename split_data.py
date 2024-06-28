import os
from argparse import ArgumentParser
import shutil

parser = ArgumentParser("BRICS data compiler")
parser.add_argument("--source_path", "-s", required=True, type=str)
parser.add_argument('--image_types', nargs='+', default=['.jpg', '.png', '.jpeg'])
args = parser.parse_args()

source_path = os.path.abspath(args.source_path)
parent_path = os.path.dirname(source_path)
out_path = os.path.join(parent_path, os.path.basename(source_path) + "_colmap")

if not os.path.exists(out_path):
    os.makedirs(out_path)

images = []

def rec_find(root):
    for file in os.listdir(root):
        _, ext = os.path.splitext(file)
        if os.path.isdir(os.path.join(root,file)):
            rec_find(os.path.join(root, file))
        elif ext in args.image_types:
            images.append(os.path.join(root,file))

rec_find(source_path)

for image in images:
    shutil.move(image, os.path.join(out_path, os.path.basename(image)))



