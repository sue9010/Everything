const cameraStream = document.getElementById("camera-stream");

cameraStream.src = `http://192.168.0.15:8080/?action=stream&user=admin&password=cg600ip100m&rtsp=rtsp://192.168.0.15:80`;
