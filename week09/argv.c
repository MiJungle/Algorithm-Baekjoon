#include <stdio.h>


char *
strchr (const char *string, int c_) {
	char c = c_;

	ASSERT (string);

	for (;;)
		if (*string == c)
			return (char *) string;
		else if (*string == '\0')
			return NULL;
		else
			string++;
}


char *
strtok_r (char *s, const char *delimiters, char **save_ptr) {
	char *token;

	ASSERT (delimiters != NULL);
	ASSERT (save_ptr != NULL);

	/* If S is nonnull, start from it.
	   If S is null, start from saved position. */
	if (s == NULL)
		s = *save_ptr;
	ASSERT (s != NULL);

	/* Skip any DELIMITERS at our current position. */
	while (strchr (delimiters, *s) != NULL) {
		/* strchr() will always return nonnull if we're searching
		   for a null byte, because every string contains a null
		   byte (at the end). */
		if (*s == '\0') {
			*save_ptr = s;
			return NULL;
		}

		s++;
	}

	/* Skip any non-DELIMITERS up to the end of the string. */
	token = s;
	while (strchr (delimiters, *s) == NULL)
		s++;
	if (*s != '\0') {
		*s = '\0';
		*save_ptr = s + 1;
	} else
		*save_ptr = s;
	return token;
}

void main(){
f_name = ["echo x y"];
char *file_name = f_name;

    strtok_r (f_name, " ", &save_ptr);
    // printf("%d\n", LOADER_SIG);
    // printf("%d\n", LOADER_ARG_CNT);
    printf("%d\n", LOADER_END);
}