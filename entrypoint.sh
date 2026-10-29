#!/bin/sh
set -e

# Ambil konfigurasi dari environment variable atau gunakan nilai default
DB_HOST="${DB_HOST:-db}"
DB_PORT="${DB_PORT:-5432}"
DB_USER="${DB_USER:-raknusantara_user}"
DB_NAME="${DB_NAME:-raknusantara_db}"

echo "Menunggu database PostgreSQL ($DB_HOST:$DB_PORT) siap..."

# Loop pengecekan koneksi ke PostgreSQL menggunakan pg_isready
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME"; do
  echo "Database belum siap, mencoba kembali dalam 2 detik..."
  sleep 2
done

echo "Database PostgreSQL berhasil terhubung! Menjalankan aplikasi..."

exec "$@"
