# 3. Buatlah Algoritma menggunakan flowchart untuk mengitung luas dan volume kubus dan balok

from graphviz import Digraph


def buat_flowchart_kubus():
    kubus = Digraph("Kubus", format="png")
    kubus.attr(rankdir="TB")

    kubus.node("A", "Mulai", shape="ellipse")
    kubus.node("B", "Masukkan sisi kubus (s)", shape="parallelogram")
    kubus.node("C", "Hitung volume = s × s × s", shape="box")
    kubus.node("D", "Hitung luas = 6 × s × s", shape="box")
    kubus.node("E", "Tampilkan luas dan volume kubus", shape="parallelogram")
    kubus.node("F", "Selesai", shape="ellipse")

    kubus.edges(["AB", "BC", "CD", "DE", "EF"])
    kubus.render("flowchart_kubus", view=True, cleanup=True)


def buat_flowchart_balok():
    balok = Digraph("Balok", format="png")
    balok.attr(rankdir="TB")

    balok.node("A", "Mulai", shape="ellipse")
    balok.node("B", "Masukkan panjang balok (p)", shape="parallelogram")
    balok.node("C", "Masukkan lebar balok (l)", shape="parallelogram")
    balok.node("D", "Masukkan tinggi balok (t)", shape="parallelogram")
    balok.node("E", "Hitung volume = p × l × t", shape="box")
    balok.node("F", "Hitung luas = 2 × ((p × l) + (p × t) + (l × t))", shape="box")
    balok.node("G", "Tampilkan luas dan volume balok", shape="parallelogram")
    balok.node("H", "Selesai", shape="ellipse")

    balok.edges(["AB", "BC", "CD", "DE", "EF", "FG", "GH"])
    balok.render("flowchart_balok", view=True, cleanup=True)


buat_flowchart_kubus()
buat_flowchart_balok()