#Inspired by : https://gist.github.com/eldondevcg/fffff4b7909351b19a53

import boto3, json, time

group_name = 'example_change_it_as_required'

# region_name = add appropiate value
client = boto3.client('logs',region_name='us-east-1')
all_streams = []

stream_batch = client.describe_log_streams(logGroupName=group_name)
all_streams += stream_batch['logStreams']
while 'nextToken' in stream_batch:
	stream_batch = client.describe_log_streams(logGroupName=group_name,nextToken=stream_batch['nextToken'])
	all_streams += stream_batch['logStreams']
	print(len(all_streams))

stream_names = [stream['logStreamName'] for stream in all_streams]

#write to text file 
out_to = open("cloudwatch_log.txt", 'w')

for stream in stream_names:
	logs_batch = client.get_log_events(logGroupName=group_name, logStreamName=stream)
	for event in logs_batch['events']:
		event.update({'group': group_name, 'stream':stream })
		out_to.write(json.dumps(event) + '\n')
	print(stream, ":", len(logs_batch['events']))
	while 'nextToken' in logs_batch:
		logs_batch = client.get_log_events(logGroupName=group_name, logStreamName=stream, nextToken=logs_batch['nextToken'])
		for event in logs_batch['events']:
			event.update({'group': group_name, 'stream':stream })
			out_to.write(json.dumps(event) + '\n')