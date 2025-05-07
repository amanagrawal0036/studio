"use client";

import { FormEvent, useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useDashboardContext } from "@/contexts/dashboard-context";
import { useToast } from "@/hooks/use-toast";

export const QueryAnswering = () => {
  const [answer, setAnswer] = useState("");
  const [messages, setMessages] = useState<
    { sender: "user" | "ai"; text: string }[]
  >([]);
  const [currentQuery, setCurrentQuery] = useState("");
  const { addQuery } = useDashboardContext();
  const { toast } = useToast();

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    if (currentQuery.trim() !== "") {
      // Add user's query to the chat
      const newMessages = [
        ...messages,
        { sender: "user", text: currentQuery },
      ];
      setMessages(newMessages);

      try {
        const result = await answerQueryFromPython(currentQuery);
        const newMessages2 = [
          ...newMessages,
          { sender: "ai", text: result },
        ];
        setMessages(newMessages2);
        addQuery({
          query: currentQuery,
          response: result,
        });
      } catch(e){
        console.log(e);
      }
      setCurrentQuery("");
    }
  };

  return (
    <Card className="space-y-4">
      <CardHeader>
        <CardTitle>💬 Query Answering</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="h-64 overflow-y-auto space-y-2">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`p-2 rounded-md ${
                message.sender === "user" ? "bg-secondary text-secondary-foreground self-end" : "bg-muted text-muted-foreground self-start"
              }`}
            >
              {message.text}
            </div>
          ))}
        </div>
        <div className="flex space-x-2">
          <Input
            type="text"
            placeholder="Ask"
            value={currentQuery}
            onChange={(e) => setCurrentQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") handleSubmit(e);
            }}
          />
          <Button onClick={handleSubmit}>Ask</Button>
        </div>
      </CardContent>
    </Card>
  );
};
