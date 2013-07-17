
module CustomHelpers
  # TODO : this is supposed to check the current url against the link's 
  # If they are the same, the link should get an "active" class 
  # So that the user can see what page they are on
  def hl_navlink(text, url)
    puts url
    puts current_page.url
    if current_page.url.index(url) != nil
      "<div class=\"active\"> #{link_to text, url} </div>"
    else
      link_to text, url
    end
  end
end
