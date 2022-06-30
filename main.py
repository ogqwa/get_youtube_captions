import json
import requests
import sys
import base64
import re

if sys.argv[1] == None:
    sys.exit()
video_id = sys.argv[1]
url = 'https://www.youtube.com/youtubei/v1/get_transcript?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
params = base64.b64encode('\n\x0b{}'.format(video_id).encode()).decode()
data = '{"context":{"client":{"clientName":"WEB","clientVersion":"2.2021111"}},"params":"%s"}' % params

res = requests.post(url, data=data, headers={'Content-type': 'application/json'})
json = res.json()
if len(json['actions']) != 0:
    data = json['actions'][0]
    captions = data['updateEngagementPanelAction']['content']['transcriptRenderer']['body']['transcriptBodyRenderer']['cueGroups']

    script = ''
    for caption in captions:
        cues = caption['transcriptCueGroupRenderer']['cues']
        for cue in cues:
            script = script + ' ' + cue['transcriptCueRenderer']['cue']['simpleText']

    normalized = ' '.join(re.sub('\[\w+\]', '', script).split())
    print(normalized)

