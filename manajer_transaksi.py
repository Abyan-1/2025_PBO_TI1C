from model import Transaksi
import database

class ManajerTransaksi:
    def tambah_transaksi(self, transaksi: Transaksi):
        sql = "INSERT INTO transaksi (deskripsi, jumlah, kategori, tanggal) VALUES (?, ?, ?, ?)"
        return database.execute_query(sql, (
            transaksi.deskripsi,
            transaksi.jumlah,
            transaksi.kategori,
            transaksi.tanggal.strftime("%Y-%m-%d")
        ))

    def ambil_semua(self):
        rows = database.fetch_query("SELECT * FROM transaksi ORDER BY tanggal DESC")
        return [Transaksi(*row[1:], id_transaksi=row[0]) for row in rows]

    def total_pemasukan(self):
        rows = database.fetch_query("SELECT SUM(jumlah) FROM transaksi")
        return rows[0][0] if rows and rows[0][0] else 0

    def per_kategori(self):
        rows = database.fetch_query("SELECT kategori, SUM(jumlah) FROM transaksi GROUP BY kategori")
        return {row[0]: row[1] for row in rows}

    def hapus_transaksi(self, id_transaksi: int):
        sql = "DELETE FROM transaksi WHERE id = ?"
        database.execute_query(sql, (id_transaksi,))
