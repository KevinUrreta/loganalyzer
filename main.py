import src._async as Async
import src._sync as Sync
import asyncio

def main ( ) -> None:
    """ Funcion principal """
    asyncio.run( Async.main( ) )
    # Sync.main( )

if __name__ == "__main__":
    try: main( )
    except KeyboardInterrupt: exit(0)
