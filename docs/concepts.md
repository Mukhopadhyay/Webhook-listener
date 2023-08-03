# Concepts involving Webhooks

## What is a webhook?

A **webhook** is a method of augmenting or altering the behavior of a web page or web application with custom callbacks. These callbacks may be maintained, modified, and managed by third-party users and developers who may not necessarily be affiliated with the originating website or application. The term "webhook" was coined by **_Jeff Lindsay_** in 2007 from the computer programming term hook.

## How are Webhooks different?

To set up a webhook, the client gives a unique URL to the server API and specifies which event it wants to know about. Once the webhook is set up, the client no longer needs to poll the server; the server will automatically send the relevant payload to the client’s webhook URL when the specified event occurs.

Webhooks are often referred to as reverse APIs or push APIs, because they put the responsibility of communication on the server, rather than the client. Instead of the client sending HTTP requests—asking for data until the server responds—the server sends the client a single HTTP POST request as soon as the data is available. Despite their nicknames, webhooks are not APIs; they work together. An application must have an API to use a webhook.

The name webhook is a simple combination of web, referring to its HTTP-based communication, and the hooking programming function that allows apps to intercept calls or other events that might be of interest. Webhooks hook the event that occurs on the server app, and prompt the server to send the payload to the client via the web. Jeff Lindsay helped to popularize the concept with his 2007 blog post, “Web hooks to revolutionize the web.”

IT teams use a variety of methods to protect apps that communicate via webhooks. Most webhook-enabled apps add a secret key to the request header of the payload, so that the client can confirm the server’s identity. Webhooks are often protected with Mutual Transport Layer Security (mTLS) authentication, which verifies both client and server before the payload is sent. It is also common for client apps to use SSL encryption for the webhook URL, to ensure the transferred data remains private.

## Examples

## References

- [Webhook - Wikipedia](https://en.wikipedia.org/wiki/Webhook)
- [What is a webhook - RedHat](https://www.redhat.com/en/topics/automation/what-is-a-webhook)
