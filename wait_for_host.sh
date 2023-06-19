#!/bin/sh
# wait-for-host.sh: Espera até que um host e porta estejam disponíveis.

set -e

host="$1"
port="$2"
timeout="${3:-15}" # tempo limite padrão de 15 segundos

echo "Aguardando $host:$port por no máximo $timeout segundos..."

until nc -z "$host" "$port"; do
  timeout=$(($timeout - 1))
  if [ $timeout -eq 0 ]; then
    echo "Falha ao aguardar $host:$port dentro do tempo limite."
    exit 1
  fi
  sleep 1
done

echo "$host:$port está disponível!"

