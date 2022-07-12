const Stream = require("node-rtsp-stream");
const streamUrl =
  "rtsp://admin:cg600ip100m@169.254.0.100/PSIA/Streaming/channels/0 : Stream 0";

stream = new Stream({
  name: "foscam_stream",
  streamUrl: streamUrl,
  wsPort: 554,
  width: 640,
  height: 480,
});
