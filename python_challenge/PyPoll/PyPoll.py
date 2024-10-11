# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
votes_percent=[]
votecount=0
candidate_list=[] #creating list unique candidate name
candidate_votes=[] #creating list to save vote count for each candidate
previous_value=0
candidate_dict={} 

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Skip the header row
    header = next(reader)
    reader1=list(reader)
       # Loop through each row of the dataset and process it
    for row in reader1:
        votecount=votecount+1
        candidate_name=row[2] #get the candidate's name from row
        if candidate_name in candidate_dict.keys(): 
             #creating dictionary to store unique candidate name and corresponding vote count
             candidate_dict[candidate_name]=candidate_dict[candidate_name]+1
        else:
            candidate_dict[candidate_name]=1
        
    # creating two lists candidate_list and candidate_votes from Dictionary
    for key,value in candidate_dict.items():
        candidate_list.append(key)
        candidate_votes.append(value)
       
 

# Open a text file to save the output

with open(file_to_output, "w") as csv_file:

    # Print the total vote count (to terminal)
    print('Election Results')
    print('--------------------------')   

    print(f'Total_Votes: {votecount}')
    print('--------------------------')   

    

    # Write the total vote count to the text file
    csv_file.write('Election Results')
    csv_file.write('\n')
    csv_file.write('--------------------------') 
    csv_file.write('\n')
    csv_file.write(f'Total Votes:{votecount}')
    csv_file.write('\n')
    csv_file.write('--------------------------') 
    csv_file.write('\n')
   


    # Loop through the candidates to determine vote percentages and identify the winner
    for i in candidate_votes :
         percent=round((i/votecount)*100,3)
         votes_percent.append(percent)


         votes_winner=max(candidate_votes) #number of maximum votes thats is going to be winning count
        # Update the winning candidate if this one has more votes
    main_list=list(zip(candidate_list,candidate_votes,votes_percent))
    for num in main_list:
         if num[1]==votes_winner:
             winner=num[0]
    # Print and save each candidate's vote count and percentage    
   
    for num in main_list:
         print(f'{num[0]}:  {num[2]}% ({num[1]})')
         csv_file.write(f'{num[0]}:  {num[2]}%   ({num[1]})')
         csv_file.write('\n')
    # Generate and print the winning candidate summary   
    # Save the winning candidate summary to the text file
    print('--------------------------')   
    print(f'Winner: {winner}')
    print('--------------------------')   
    csv_file.write('--------------------------')
    csv_file.write('\n')
    csv_file.write(f'Winner: {winner}')
    csv_file.write('\n')
    csv_file.write('--------------------------')
    