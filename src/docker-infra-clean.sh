# Delete networking
echo "Deleting network for docker..."
docker network rm data-platform-network
echo "Done!"

# Delete all Containers
echo "Deleting container..."
docker rm -f $(docker ps -a -q)
echo "Done!"

# Delete all volumes
echo "Deleting volume..."
docker volume rm $(docker volume ls -q)
echo "Done!"