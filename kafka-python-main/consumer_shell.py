import os
shell_command = 'c:/kafka212/bin/windows/kafka-console-consumer.bat --topic topic1 --from-beginning --max-messages 20 --timeout-ms 60000 --bootstrap-server localhost:9092'
output = list(filter(None, os.popen(shell_command).read().split("\n")))
for messages in output :
    print(messages, end="\n")