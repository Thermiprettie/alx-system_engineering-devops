#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	int t = 0;
	pid_t zomb_p = 0;

	for (t = 0; t < 5; t++)
	{
		zomb_p = fork();

		if (zomb_p > 0)
			printf("Zombie process created, PID: %d\n", zomb_p);
		else
			exit(0);

	}

	return (infinite_while());
}
