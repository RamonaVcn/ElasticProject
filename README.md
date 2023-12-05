openapi: 3.0.0
info:
  title: Movie Search API
  description: API for searching movies
  version: 1.0.0

paths:
  /movies:
    get:
      summary: Get a list of movies
      parameters:
        - name: query
          in: query
          description: Filter movies by title
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              example:
                movies:
                  - id: 1
                    title: "Inception"
                    genres: "Sci-Fi, Action"
                    release_date: "2010-07-16"
                  - id: 2
                    title: "The Dark Knight"
                    genres: "Action, Crime, Drama"
                    release_date: "2008-07-18"

  /movies/{movieId}:
    parameters:
      - name: movieId
        in: path
        required: true
        description: ID of the movie
        schema:
          type: integer
    get:
      summary: Get details of a specific movie
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              example:
                id: 1
                title: "Inception"
                genres: "Sci-Fi, Action"
                release_date: "2010-07-16"
        '404':
          description: Movie not found

components:
  schemas:
    Movie:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        genres:
          type: string
        release_date:
          type: string
          format: date



MAPPING:
PUT /movies
{
  "mappings": {
    "properties": {
      "id": {"type": "integer"},
      "title": {"type": "text"},
      "genres": {"type": "text"},
      "release_date": {"type": "date", "format": "yyyy-MM-dd"}
    }
  }
}

