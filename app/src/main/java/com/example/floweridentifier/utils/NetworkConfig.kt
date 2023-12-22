package com.example.floweridentifier.utils

import com.example.floweridentifier.data.model.User

object NetworkConfig {
    const val BASE_URL = "https://config.phucanhthanh.com/api/v1/"

    // Default chat gpt3 api key, update when open app
    var OPEN_API_KEY = "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"

    // Mock data for chat gpt
    val botUser = User("Bot", false, 0)
    val felixUser = User("Felix", true, 0)
}