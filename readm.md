Previous pagination:

<nav aria-label="Navigation">
    
    <ul class="pagination">
        {% if page_obj.has_previous %}
            <li class="page-item"><a class="page-link" href="?page=1&amp;{{ view.urlencode_filter }}">&laquo; first</a></li>
            <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}&amp;{{ view.urlencode_filter }}">previous</a></li>
        {% endif %}



        {% if page_obj.has_next %}
            <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}&amp;{{ view.urlencode_filter }}">next</a></li>
            <li class="page-item"><a class="page-link" href="?page={{ page_obj.paginator.num_pages }}&amp;{{ view.urlencode_filter }}">last &raquo;</a></li>
        {% endif %}
  </ul>
    </nav>
    <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>