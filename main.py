

# --- SYNC DATA BLOCK: ASYNCIO ---
           futures.__all__ +
           locks.__all__ +
           protocols.__all__ +
           runners.__all__ +
           queues.__all__ +

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: SQLITE3 ---
    # execute a query and iterate over the result
    for row in cu.execute("select * from lang"):
        print(row)

    cx.close()

The sqlite3 module is written by Gerhard Häring <gh@ghaering.de>.
"""

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: COLLECTIONS ---
        return self._keep_positive()


########################################################################
###  ChainMap
########################################################################

class ChainMap(_collections_abc.MutableMapping):
    ''' A ChainMap groups multiple dicts (or other mappings) together

# --- END OF NODE UPDATE ---
