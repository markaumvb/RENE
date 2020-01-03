# Replication package

This site contains scripts and datas to reproduce the paper intituled: Pull Requests or Commits? Which Method Should We Use to Study Contributors’ Behavior?

## Guidelines

### Selecting the projects

All projects used in this paper is available on this [link](https://github.com/markaumvb/RENE/blob/master/data/projects) 

### Collecting data

All data collected to our paper was builded in python, and stored in a MYSQL database.

1. Create the database structure to be used for the collection [tables structure](https://github.com/markaumvb/RENE/tree/master/database%20script)

2. Before executing the script it is necessary to make some presets:
Set the variables GH_USER and GH_PASSWD with your github platform user data (github registration required). set the LANGUAGE variable with the language of the project to be collected.

2. For eache project, run the script [get_pr](https://github.com/markaumvb/RENE/blob/master/python_script/get_pr.py): 

```markdown
  get_pr('project_owner', 'project_name')
```
3. Run others scripts, available [here](https://github.com/markaumvb/RENE/tree/master/python_script)
