# Create networking
echo "Create networking for docker..."
docker network create data-platform-network
echo "Create network successfully..."

# Create Volume
echo "Create shared workspace..."
docker volume create --name=hadoop-distributed-file-system
echo "Create shared workspace successfully..."