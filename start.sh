DIR="./kafka-docker"
pwd
if [ ! -d "$DIR" ]; then
  git clone "git@github.com:wurstmeister/kafka-docker.git"
fi

cp './config/docker-compose.yml' './kafka-docker/docker-compose.yml'
cd $DIR || exit
docker-compose up -d
