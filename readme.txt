This is the readme for MemeBot.

MemeBot generates a random phrase over a random meme image, transforming that
image in a random way.

MemeBot Structure:
-Generate random text
-Gather image
-User can choose to apply random transformation to image
-Apply text to random image
-Returns meme
-Data gathering of text and image libraries
-Optional: Hot or not voting system to filter best memes.

Generating Random Text:
-Gather library of words (from Data Gathering)
-Create model for text generation
-Generate sentence to apply to image

Apply Text to Random Image:
-Gather image from library of images (from Data Gathering)
-Apply image transformation if chosen
-Make image from text (proper meme font), then apply to image
-Saves new meme image.

Optional: Hot or Not:
-Make display framework for comparitive images
-User votes on image:
    -How is vote registered? How is vote stored?
    -Aggregate voting structure? Keeps all votes given to it.
-Compare vote results to generate top 5(?) memes.
