from github import Github

### To use this file: ##############################################################################################################################################################
##     	First, make a new directory and cd into it
##
##		Then, paste this command and run it:
##	     	git clone https://github.com/awslabs/open-data-registry.git
##		
##		Third, you will need to create a branch to store your work:
##			git branch <branchname>
##			git checkout <branchname>
##
##		Last, put this file in the "open-data-registry" directory and run it:
##			python3 bulk_github_write.py
##
###################################################################################################################################################################################

# check to see if there is our github repo locally
import os

folder_path = "open-data-registry"

if not os.path.isdir(folder_path):
    print("STOP.  Please git clone the repo in a folder and put this file in that folder at the root.")
    exit()

# iterate through all the noaa- filenames (locally from the git repo)
import os

folder_path = "open-data-registry/datasets/"
noaa_files = []
git_files = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
    	if (file.startswith("noaa-")):
    		noaa_files.append(os.path.join(root, file))
    		git_files.append("datasets/"+file)

# new value for the License key
new_license = "NOAA data disseminated through NODD is made available under the \"[Creative Commons 1.0 Universal Public Domain Dedication (CC0-1.0) license]https://creativecommons.org/publicdomain/zero/1.0/?ref=chooser-v1\", which is well-known and internationally recognized. There are no restrictions on the use of the data. The data are open to the public and can be used as desired."

# iterate through the files, opening each for writing
import json
import yaml

for file in noaa_files:
	data = ""

	with open(file, 'r') as f:
		data = yaml.safe_load(f)

	# change only the License key to the new value
	data.update({'License': new_license})

	# Write the updated data back to the file
	with open(file, 'w') as f:
	    yaml.dump(data, f, default_flow_style=False)


# git add all the files
import os

# Get the current working directory
print(os.getcwd())

# Change the working directory
os.chdir(os.getcwd() + "/open-data-registry")

# Verify the change
print(os.getcwd()) 

# add all our changes to be tracked by git
for file in git_files:
	os.system("git add {}".format(file))
	print("git add {}".format(file))


# git commit the change to the branch
os.system('git commit -m \"bulk update of NOAA license\"')

print(" ")
print("Done.  Run the following command to push your changes:")
print("gh pr create --title \"message\"")
