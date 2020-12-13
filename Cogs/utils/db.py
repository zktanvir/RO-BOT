import aiosqlite


async def connect_db():
	conn = await aiosqlite.connect("./db/info.db")
	conn.row_factory = aiosqlite.Row
	return conn


async def add_prefix(guild_id, prefix):
	conn = await connect_db()
	c = await conn.cursor()
	await c.execute("INSERT OR IGNORE INTO prefix VALUES(?,?);", (
	    guild_id,
	    prefix,
	))
	await conn.commit()
	await conn.close()

async def set_prefix(guild_id,prefix):
	conn = await connect_db()
	c = await conn.cursor()
	await c.execute("UPDATE prefix SET prefix=? WHERE guild_id=?",(prefix,guild_id,))
	await conn.commit()
	await conn.close()
	

async def prefix(guild_id):
	conn = await connect_db()
	c = await conn.cursor()
	await c.execute(
	    "SELECT * FROM prefix WHERE guild_id=?",
	    (guild_id,)
	)
	#await conn.close()
	result = await c.fetchone()
	#prefix = result[1]
	if result is None:
		await add_prefix(guild_id,"Ro ")
		return "Ro "
	prefix = result[1]
	return prefix
