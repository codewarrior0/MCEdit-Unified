This file will contain a list of all the methods of the level parameter.

## MCInfdevOldLevel

### Properties

| Property Name | Description |
| ------------- | ----------- |
| materials | The type of materials the world uses (Usually alphaMaterials) |
| RandomSeed | The seed of the current world as defined in level.dat |
| LevelName | The name of the world as defined in level.dat |
| GameType | The gamemode the world is set to |

### Functions

| Function name | Arguments | Description |
| ------------- | --------- | ----------- |
| __init__ | filename, create, random_seed, last_played, readonly, workFolderPath, x | Load an Alpha level from the given filename. It can point to eithera level.dat or a folder containing one. If create is True, it will also create the world using the random_seed and last_played arguments. If they are none, a random 64-bit seed will be selected for RandomSeed and long(time.time() * 1000) will be used for LastPlayed. If you try to create an existing world, its level.dat will be replaced. |
| __str__ |  | **Undocumented** |
| _create | filename, random_seed, last_played, root_tag | **Undocumented** |
| _dirhash | n, s | **Undocumented** |
| _generateLightsIter | dirtyChunkPositions, la, dirtyChunks, workDone, workTotal, progressInfo, i, chunk, ch, cx, cz, dx, dz, zeroChunk, startingDirtyChunks, oldLeftEdge, oldBottomEdge, oldChunk, lights, clipLight, j, light, zerochunkLight, newDirtyChunks, work, neighboringChunks, dir, chunkLa, chunkLight, nc, ncLight, newlight | **Undocumented** |
| _getChunkBytes | cx, cz | **Undocumented** |
| _getChunkData | cx, cz, chunkData, data, root_tag, e | **Undocumented** |
| _getFakeChunkEntities | cx, cz, i, e, ent, x, y, z, ecx, ecz | distribute entities into sublists based on fake chunk position _fakeEntities keys are (cx, cz) and values are (Entities, TileEntities, TileTicks) |
| _getSlices | box, getAllSlices | **Undocumented** |
| _isLevel | cls, filename, f, files | **Undocumented** |
| _oldChunkFilename | cx, cz | **Undocumented** |
| _storeLoadedChunkData | chunkData, ocx, ocz, oldChunkData, data | **Undocumented** |
| acquireSessionLock | lockfile, f | **Undocumented** |
| addEntities | entities, e | **Undocumented** |
| addEntity | entityTag, x, y, z, chunk | **Undocumented** |
| addTileEntity | tileEntityTag, x, y, z, chunk | **Undocumented** |
| addTileTick | tickTag, x, y, z, chunk | **Undocumented** |
| addTileTicks | tileTicks, e | **Undocumented** |
| adjustExtractionParameters | box, x, y, z, w, h, l, destX, destY, destZ | **Undocumented** |
| biomeAt | x, z, biomes, xChunk, zChunk | **Undocumented** |
| blockAt | x, y, z, zc, xc, xInChunk, zInChunk, ch | returns 0 for blocks outside the loadable chunks.  automatically loads chunks. |
| blockDataAt | x, y, z, zc, xc, xInChunk, zInChunk, ch | **Undocumented** |
| blockLightAt | x, y, z, zc, xc, xInChunk, zInChunk, ch | **Undocumented** |
| checkSessionLock | lockfile, lock | **Undocumented** |
| close |  | Unload all chunks and close all open filehandles. Discard any unsaved data. |
| containsChunk | cx, cz | **Undocumented** |
| containsPoint | x, y, z | **Undocumented** |
| copyBlocksFrom | destLevel, sourceLevel, sourceBox, destinationPoint, blocksToCopy, entities, create, biomes, tileTicks, staticCommands, moveSpawnerPos, first | **Undocumented** |
| copyBlocksFromIter | destLevel, sourceLevel, sourceBox, destinationPoint, blocksToCopy, entities, create, biomes, tileTicks, staticCommands, moveSpawnerPos, regenerateUUID, first, lx, ly, lz, startTime, destBox, chunkCount, i, e, t, tt, sourceMask, s, d, copyOffset, destCpos, cx, cz, destChunkBox, o, destChunkBoxInSourceLevel, destChunk, srcCpos, sourceChunk, sourceChunkBox, sourceSlices, _, destSlices, sourceBlocks, sourceData, convertedSourceBlocks, convertedSourceData, ents, entityTag, eTag, copy, tileEntities, tileEntityTag, tileTicksList, tileTick | copy blocks between two infinite levels by looping through the destination's chunks. make a sub-box of the source level for each chunk and copy block and entities in the sub box to the dest chunk. |
| copyChunkFrom | world, cx, cz, destChunk, sourceChunk, chunkData, data, sourceFolder | Copy a chunk from world into the same chunk position in self. |
| createChunk | cx, cz | **Undocumented** |
| createChunks | chunks, i, ret, cx, cz | **Undocumented** |
| createChunksInBox | box | **Undocumented** |
| createPlayer | playerName, playerTag, i | **Undocumented** |
| deleteChunk | cx, cz | **Undocumented** |
| deleteChunksInBox | box, i, ret, cx, cz | **Undocumented** |
| dirhash | n | **Undocumented** |
| extractAnySchematic | level, box | **Undocumented** |
| extractAnySchematicIter | level, box, i | **Undocumented** |
| extractChunk | cx, cz, parentFolder, chunkFilename, outputFile, chunk | **Undocumented** |
| extractChunksInBox | box, parentFolder, cx, cz | **Undocumented** |
| extractSchematic | sourceLevel, box, entities | **Undocumented** |
| extractSchematicIter | sourceLevel, box, entities, p, newbox, destPoint, tempSchematic, i | **Undocumented** |
| extractZipSchematic | sourceLevel, box, zipfilename, entities | **Undocumented** |
| extractZipSchematicIter | sourceLevel, box, zipfilename, entities, p, sourceBox, destPoint, tempSchematic, i | **Undocumented** |
| fakeBlocksForChunk | cx, cz, cxOff, czOff, b | **Undocumented** |
| fakeDataForChunk | cx, cz, cxOff, czOff | **Undocumented** |
| fillBlocks | level, box, blockInfo, blocksToReplace, noData | **Undocumented** |
| fillBlocksIter | level, box, blockInfo, blocksToReplace, noData, chunkIterator, changesLighting, blocktable, newAbsorption, b, oldAbsorptions, a, newEmission, oldEmissions, tileEntity, tileEntityName, block, blocksIdToReplace, blocksList, boxX, boxY, boxZ, i, skipped, replaced, chunk, slices, blocks, data, needsLighting, blockCount, include, position, tileEntityObject | **Undocumented** |
| flipEastWest |  | **Undocumented** |
| flipNorthSouth |  | **Undocumented** |
| flipVertical |  | **Undocumented** |
| generateLights | dirtyChunkPositions | **Undocumented** |
| generateLightsIter | dirtyChunkPositions, startTime, maxLightingChunks, chunkLists, splitChunkLists, a, estimatedTotals, workDone, i, dc, workTotal, t, c, p, timeDelta | dirtyChunks may be an iterable yielding (xPos,zPos) tuples if none, generate lights for all chunks that need lighting |
| getAllChunkSlices | slices, box, x, y, z, cpos, xPos, zPos, chunk | **Undocumented** |
| getChunk | cx, cz, chunk, k, ch, chunkData | read the chunk from disk, load it, and return it. |
| getChunkSlices | box | **Undocumented** |
| getChunks | chunks | pass a list of chunk coordinate tuples to get an iterator yielding AnvilChunks. pass nothing for an iterator of every chunk in the level. the chunks are automatically loaded. |
| getDimension | dimNo, dim | **Undocumented** |
| getEntitiesInBox | box, entities, chunk, slices, point | **Undocumented** |
| getPlayerDimension | player, playerTag | **Undocumented** |
| getPlayerGameType | player, playerTag | **Undocumented** |
| getPlayerOrientation | player, yp, y, p | returns (yaw, pitch) |
| getPlayerPath | player | **Undocumented** |
| getPlayerPosition | player, playerTag, posList, x, y, z | **Undocumented** |
| getPlayerTag | player, playerFilePath, playerTag | **Undocumented** |
| getRegionForChunk | cx, cz | **Undocumented** |
| getTileEntitiesInBox | box, tileEntites, chunk, slices, point | **Undocumented** |
| getTileTicksInBox | box, tileticks, chunk, slices, point | **Undocumented** |
| getWorldBounds | allChunks, mincx, maxcx, mincz, maxcz, origin, size | **Undocumented** |
| heightMapAt | x, z, zc, xc, xInChunk, zInChunk, ch, heightMap | **Undocumented** |
| init_player_data | player_data, p, player_data_file, data | **Undocumented** |
| init_scoreboard | root_tag | **Undocumented** |
| isLevel | cls, filename, f, data, root_tag | Tries to find out whether the given filename can be loaded by this class.  Returns True or False. Subclasses should implement _isLevel, _isDataLevel, or _isTagLevel. |
| listDirtyChunks | cPos, chunkData | **Undocumented** |
| loadLevelDat | create, random_seed, last_played, e, filename_old | **Undocumented** |
| markDirtyBox | box, cx, cz | **Undocumented** |
| markDirtyChunk | cx, cz | **Undocumented** |
| playerSpawnPosition | player, dataTag, playerSpawnTag, i | xxx if player is None then it gets the default spawn position for the world if player hasn't used a bed then it gets the default spawn position |
| preloadChunkPositions |  | **Undocumented** |
| preloadDimensions | worldDirs, dirname, dimNo, dim, e | **Undocumented** |
| removeEntitiesInBox | box, count, chunk, slices, point | **Undocumented** |
| removeTileEntities | func, newEnts, ent, entsRemoved | **Undocumented** |
| removeTileEntitiesInBox | box, count, chunk, slices, point | **Undocumented** |
| removeTileTicks | func, newEnts, ent, entsRemoved | **Undocumented** |
| removeTileTicksInBox | box, count, chunk, slices, point | **Undocumented** |
| roll |  | **Undocumented** |
| rotateLeft |  | **Undocumented** |
| saveInPlace | gen, _ | **Undocumented** |
| saveInPlaceGen | level, _, dirtyChunkCount, chunk, cx, cz, data, path, tag, file_ | **Undocumented** |
| save_player_data | player_data, p | **Undocumented** |
| save_scoreboard | score | **Undocumented** |
| setBiomeAt | x, z, biomeID, biomes, xChunk, zChunk | **Undocumented** |
| setBlockAt | x, y, z, blockID, zc, xc, xInChunk, zInChunk, ch | returns 0 for blocks outside the loadable chunks.  automatically loads chunks. |
| setBlockDataAt | x, y, z, newdata, zc, xc, xInChunk, zInChunk, ch | **Undocumented** |
| setBlockLightAt | x, y, z, newLight, zc, xc, xInChunk, zInChunk, ch | **Undocumented** |
| setPlayerAbilities | gametype, player, playerTag | **Undocumented** |
| setPlayerDimension | d, player, playerTag | **Undocumented** |
| setPlayerGameType | gametype, player, playerTag | **Undocumented** |
| setPlayerOrientation | yp, player, p | **Undocumented** |
| setPlayerPosition | .1, player, x, y, z, p, posList, playerTag | **Undocumented** |
| setPlayerSpawnPosition | pos, player, playerSpawnTag, name, val | xxx if player is None then it sets the default spawn position for the world |
| setSkylightAt | x, y, z, lightValue, zc, xc, xInChunk, zInChunk, ch, skyLight, oldValue | **Undocumented** |
| skylightAt | x, y, z, zc, xc, xInChunk, zInChunk, ch | **Undocumented** |
| tileEntityAt | x, y, z, chunk | **Undocumented** |
| unload |  | Unload all chunks and close all open filehandles. |


