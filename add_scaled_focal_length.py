import numpy as np 

before_smooth = np.load(
    "driving_videos/your_video_1/smpl_results/smpls_group.npz", 
    allow_pickle=True
)

after_smooth = np.load(
    "driving_videos/your_video_1/smpl_results/smooth_smpls_group.npz",
    allow_pickle=True
)

smpl = after_smooth["smpl"]
camera = after_smooth["camera"]
scaled_focal_length = before_smooth["scaled_focal_length"]

np.savez(
    "driving_videos/your_video_1/smpl_results/smpls_group.npz",
    smpl=smpl,
    camera=camera,
    scaled_focal_length=scaled_focal_length
)
