import { useState, useRef, useEffect } from "react";
import axios from "axios";

function App() {
	const [messages, setMessages] = useState([]);
	const [input, setInput] = useState("");
	const [userId, setUserId] = useState("u001");
	const [loading, setLoading] = useState(false);
	const chatRef = useRef(null);

	const handleSend = async () => {
		if (!input.trim()) return;

		const newMessage = { sender: "user", text: input };
		setMessages((prev) => [...prev, newMessage]);
		setInput("");
		setLoading(true);

		try {
			const res = await axios.post("http://localhost:8000/chat", {
				user_id: userId,
				message: input,
			});

			const botMessage = {
				sender: "bot",
				text: res.data.response,
				source: res.data.query_type,
			};

			setMessages((prev) => [...prev, botMessage]);
		} catch (err) {
			console.error("Request failed:", err);
			setMessages((prev) => [
				...prev,
				{ sender: "bot", text: "Something went wrong." },
			]);
		} finally {
			setLoading(false);
		}
	};

	// Auto-scroll to bottom
	useEffect(() => {
		chatRef.current?.scrollTo({
			top: chatRef.current.scrollHeight,
			behavior: "smooth",
		});
	}, [messages]);

	return (
		<div className="min-h-screen bg-[#212121] text-white flex flex-col">
			{/* Chat content wrapper */}
			<div className="flex-1 flex flex-col max-w-4xl w-full mx-auto">
				{/* Chat History */}
				<div
					ref={chatRef}
					className="flex-1 overflow-y-auto px-4 py-6 space-y-4"
				>
					{messages.map((msg, idx) => (
						<div
							key={idx}
							className={`flex w-full ${
								msg.sender === "user" ? "justify-end" : "justify-start"
							}`}
						>
							<div
								className={`${
									msg.sender === "user"
										? "bg-[#303030] text-white"
										: "bg-[#212121] text-white"
								} rounded-xl px-4 py-2 inline-block whitespace-pre-wrap max-w-[80%]`}
							>
								{msg.text}
								{msg.source && msg.sender === "bot" && (
									<p className="text-xs italic text-gray-400 mt-1">
										Source: {msg.source}
									</p>
								)}
							</div>
						</div>
					))}
				</div>

				{/* Fixed input bar at the bottom */}
				<div className="border-t border-[#333] px-4 py-3 bg-[#212121]">
					<div className="relative w-full">
						<input
							className="w-full bg-[#303030] text-white rounded-xl p-3 pr-16 focus:outline-none"
							value={input}
							onChange={(e) => setInput(e.target.value)}
							onKeyDown={(e) => e.key === "Enter" && handleSend()}
							placeholder="Ask a question..."
						/>
						<button
							onClick={handleSend}
							disabled={loading}
							className="absolute right-3 top-1/2 -translate-y-1/2 bg-[#10a37f] text-white px-4 py-1 rounded-lg text-sm"
						>
							{loading ? "..." : "Send"}
						</button>
					</div>
				</div>
			</div>
		</div>
	);
}

export default App;
