C=$1

if [ -z "$1" ]; 
then
	C=$(date +%F__%T)
fi

echo git pull origin master
git pull origin master
echo git add --all :/
git add --all :/
echo git commit -m "${C}"
git commit -m "${C}"
echo git push origin master
git push origin master

echo "Done!..."
