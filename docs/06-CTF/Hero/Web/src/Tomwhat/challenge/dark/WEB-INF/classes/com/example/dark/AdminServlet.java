package com.example.dark;

import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.*;

public class AdminServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        resp.setContentType("text/html;charset=UTF-8");

        HttpSession s = req.getSession(false);
        String username = s == null ? null : (String) s.getAttribute("username");

        StringBuilder html = new StringBuilder("<html><body><h1>Admin Panel</h1>");

        if ("darth_sidious".equalsIgnoreCase(username)) {
            html.append("<p>Welcome Lord Sidious, Vador says: Hero{fake_flag}.</p>");
        } else {
            html.append("<p>Access denied.</p>");
        }

        html.append("</body></html>");
        resp.getWriter().write(html.toString());
    }
}
