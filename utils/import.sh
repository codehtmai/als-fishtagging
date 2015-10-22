export PGPASSWORD=@Django!
for TT in $(mdb-tables Tags25.mdb); do
mdb-export -I postgres -q \' Tags25.mdb $TT | psql -d fishtagging_import -U djangodb -h 192.168.1.11
done

