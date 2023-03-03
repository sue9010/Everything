import cv2
from onvif import ONVIFCamera

# Connect to the camera
mycam = ONVIFCamera('192.168.0.15', 80, 'admin', 'cg600ip100m','/etc/onvif/wsdl/')
media = mycam.create_media_service()

# Retrieve the list of profiles
profiles = media.GetProfiles()

# Choose a profile
profile = profiles[0]

# Retrieve the snapshot URI
snapshot_uri = media.GetSnapshotUri(ProfileToken=profile.token).Uri

# Retrieve the image data
image = cv2.imread(snapshot_uri)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
