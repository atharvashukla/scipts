import argparse
import moviepy.editor as mp

def create_video_from_image(image_path, duration, output_path):
    image_clip = mp.ImageClip(image_path, duration=duration)
    image_clip.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac', ffmpeg_params=["-pix_fmt", "yuv420p"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a video from an image with the specified duration.')
    parser.add_argument('image_path', type=str, help='Path to the image file.')
    parser.add_argument('duration', type=int, help='Duration of the video in seconds.')
    parser.add_argument('output_path', type=str, help='Path to the output video file.')

    args = parser.parse_args()
    create_video_from_image(args.image_path, args.duration, args.output_path)
