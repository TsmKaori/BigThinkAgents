import argparse as ap 
import numpy as np 
import matplotlib.pyplot as mp 


#Function to parse lines of relevant data into triples in format : (mean reward, standard deviation, time)
def parse_lines(lines):
    triple_array = [] # will hold all parsed triples
    for line in lines:
        #get Time Elapsed
        time_start = line.find("Elapsed: ")
        time_substr = line[time_start+len("Elapsed: "):] # this strips off everything before time
        time_end = time_substr.find(" ")
        time_elapsed = float(time_substr[:time_end]) # this strips off the remainder of the data

        #get mean_reward
        reward_start = line.find("Mean Reward: ")
        reward_substr = line[reward_start+len("Mean Reward: "):]
        reward_end = reward_substr.find(" ")
        reward = float(reward_substr[:reward_end-1]) # -1 is to remove trailing dot

        #get standard deviation of reward
        dev_start = line.find("of Reward: ")
        dev_substr = line[dev_start+len("of Reward: "):]
        dev_end = dev_substr.find(" ")
        dev = float(dev_substr[:dev_end-1])

        #append to array
        triple_array.append((reward, dev, time_elapsed))
    return triple_array


#Setup command line arguments, afterwards args.data holds the file name
parser = ap.ArgumentParser()
parser.add_argument("data", help="The file containing the relevant data.")
args = parser.parse_args()

file = open(args.data, "r")
data = file.readlines()
# Get relevant lines out of terminal output
relevant_lines = [line for line in data if line.find("Reward: ") >= 0]

#Parse relevant lines into triples of data
data_triples = parse_lines(relevant_lines)

#Split triples into arrays to use as axes
avg_reward_data = [triple[0] for triple in data_triples]
std_reward_data = [triple[1] for triple in data_triples]
time_elapsed = [triple[2] for triple in data_triples]

#Plot
mp.plot(time_elapsed, std_reward_data)
mp.xlabel('Time (s)')
mp.ylabel('Standard Deviation')
mp.savefig("std_dev.png")

#Clear plot, make new plot
mp.clf()

mp.plot(time_elapsed, avg_reward_data)
mp.xlabel('Time (s)')
mp.ylabel('Average Reward')
mp.savefig('avg_reward.png')



