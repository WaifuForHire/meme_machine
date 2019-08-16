# Meme

import argparse
import video_loader as vl

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to the video to scan.")

args = vars(ap.parse_args())

ld = vl.loader(args["video"])
while not ld.complete():
    fname = ld.get_next_frame()
    print("frame grabbed: ", fname)
    ld.flush_temp()

print("video file completed")
