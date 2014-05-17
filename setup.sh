head -n1000 data/original/projects.csv > data/small/projects_h1000.csv
head -n1000 data/original/outcomes.csv > data/small/outcomes_h1000.csv
head -n1000 data/original/resources.csv > data/small/resources_h1000.csv
head -n1000 data/original/essays.csv > data/small/essays_h1000.csv
#sed 's/^M//g' data/original/essays_h1000.csv > data/original/essays_h1000.csv # this is needed for reading this file in Excel

head -n1 data/original/projects.csv > data/small/projects_t1000.csv
tail -n1000 data/original/projects.csv >> data/small/projects_t1000.csv

head -n1 data/original/outcomes.csv > data/small/outcomes_t1000.csv
tail -n1000 data/original/outcomes.csv >> data/small/outcomes_t1000.csv