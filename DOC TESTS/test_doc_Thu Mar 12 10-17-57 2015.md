## AnvilChunk

 This is a 16x16xH chunk in an (infinite) world.
    The properties Blocks, Data, SkyLight, BlockLight, and Heightmap
    are ndarrays containing the respective blocks in the chunk file.
    Each array is indexed [x,z,y].  The Data, Skylight, and BlockLight
    arrays are automatically unpacked from nibble arrays into byte arrays
    for better handling.
    

## AnvilChunkData

 This is the chunk data backing an AnvilChunk. Chunk data is retained by the MCInfdevOldLevel until its
    AnvilChunk is no longer used, then it is either cached in memory, discarded, or written to disk according to
    resource limits.

    AnvilChunks are stored in a WeakValueDictionary so we can find out when they are no longer used by clients. The
    AnvilChunkData for an unused chunk may safely be discarded or written out to disk. The client should probably
     not keep references to a whole lot of chunks or else it will run out of memory.
    

## AnvilWorldFolder

None

## BoundingBox

None

## ChunkAccessDenied

Exception that is raised when a chunk is trying to be read from disk while
    saving is taking place

## ChunkBase

None

## ChunkConcurrentException

Exception that is raised when a chunk is being modified while
    saving is taking place

## ChunkMalformed

None

## ChunkNotPresent

None

## ChunkedLevelMixin

None

## Entity

None

## EntityLevel

Abstract subclass of MCLevel that adds default entity behavior

## LightedChunk

None

## MCAlphaDimension

None

## MCInfdevOldLevel

None

## MCLevel

 MCLevel is an abstract class providing many routines to the different level types,
    including a common copyEntitiesFrom built on class-specific routines, and
    a dummy getChunk/allChunks for the finite levels.

    MCLevel subclasses must have Width, Length, and Height attributes.  The first two are always zero for infinite levels.
    Subclasses must also have Blocks, and optionally Data and BlockLight.
    

## MCRegionFile

None

## PlayerNotFound

None

## SessionLockLost

None

## TileEntity

None

## TileTick

None

## _ZeroChunk

 a placebo for neighboring-chunk routines 

## datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints or longs.


