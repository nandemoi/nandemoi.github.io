for i in `git verify-pack -v .git/objects/pack/$1.idx | sort -k 3 -n | tail -10 | cut -f1`; do
    git rev-list --objects --all | grep $i | cut -d" " -f2
done >> cleanpack.txt

echo "" > cleanlist.txt
for i in `cat cleanlist.txt`; do
    ls $i > /dev/null 2>&1
    if [ $? -eq 1 ]; then
        echo $i >> cleanlist.txt
    fi
done

git filter-branch --index-filter 'git rm --cached --ignore-unmatch `cat cleanlist.txt`' -- --all
rm -Rf .git/refs/original
rm -Rf .git/logs/
git gc --aggressive --prune=now