
import sys

input_audio = sys.argv[1]
output_audio = sys.argv[2]
slides = sys.argv[3]

print(input_audio)
print(output_audio)
print(slides)

with open(input_audio,'rb') as file:
    lines = file.readlines()

Batch = int(slides)
end = 0
for i in range(1, Batch + 1):
    if i == 1:
        start = 0
    increase = int(len(lines) / Batch)
    end = end + increase
    with open(output_audio + "_SplitFile_" + str(i) + ".mp3",'wb') as file:
        for line in lines[start:end]:
            file.write(line)
    
    start = end
