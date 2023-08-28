import DiscordRPC

rpc = DiscordRPC.RPC.Set_ID(app_id=975275670345228358)

rpc.set_activity(
      state="Spotify App",
      details="Driving on the I-95",
      large_image="android_auto_logo",
      small_image="spotify_app_logo_svg"
    )

rpc.run()