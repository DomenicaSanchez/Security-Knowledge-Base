package com.example.dark;

import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.*;

public class DarkServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        resp.setContentType("text/html;charset=UTF-8");

        HttpSession s = req.getSession(false);
        String username = s == null ? null : (String) s.getAttribute("username");

        StringBuilder html = new StringBuilder();
        html.append("<html><body><h1>Dark Side</h1>");

        if (username == null)
            html.append("<p>Welcome to the dark side Darth Not Already Sidious.</p>");
        else
            html.append("<p>Welcome to the dark side Darth ").append(username).append("</p>");

        html.append("<a href='admin'>Admin interface</a>");

        html.append("</body></html>");
        resp.getWriter().write(html.toString());
    }
}
