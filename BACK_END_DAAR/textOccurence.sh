cat 56667-0.txt| awk -F '[^A-Za-z]' '{for (i=1;i<=NF;i++) {if (length($i)>2) {tab[$i]++}}} END {for (token in tab) {print token " " tab[token]}}'
