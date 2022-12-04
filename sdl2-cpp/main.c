#include <SDL2/SDL.h>
#include <stdio.h>

const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;

int main (int argc, char *argv[])
{
	SDL_Window* window = NULL;
	SDL_Surface* screenSurface = NULL;

	// init
	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		printf("COULD NOT BE INIT, SDL_ERROR: %s\n", SDL_GetError());
	}
	else {
        // create window
        window = SDL_CreateWindow( "voronoi sdl c++ aaa", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, 0);

        if(window == NULL) {
            printf( "WINDOW COULD NOT BE CREATED, SDL_Error: %s\n", SDL_GetError() );
		} else {
			screenSurface = SDL_GetWindowSurface(window);
			
			// fill surface
			SDL_FillRect(screenSurface, NULL, SDL_MapRGB(screenSurface -> format, 0xFF, 0xFF, 0xFF));

			// update
			SDL_UpdateWindowSurface(window);

			SDL_Delay(5000);
			SDL_Quit();
		}
	}
	return 0;
}
