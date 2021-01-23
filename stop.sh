DIR="./kafka-docker"
if [  -d "$DIR" ]; then
  cd $DIR || exit
  # Take action if $DIR exists. #
  docker-compose stop
fi