from config import config


def get_item_info(response):
    info_keys = list()
    info_values = list()
    info_containers = response.css(config.get("info_containers_css"))
    
    for info in info_containers:
        temp_info_key = info.xpath(config.get("info_key")).get()
        info_key = " ".join(temp_info_key.split())
        info_value_container = info.css(config.get("info_val_container"))
        if info_value_container.xpath(config.get("info_val_checkbox")):
            if info_value_container.xpath(config.get("info_val_checkbox_content")):
                info_val = 1
            else:
                info_val = 0
        else:
            info_val = info_value_container.xpath(config.get("info_val_text_content")).get() 

        info_keys.append(info_key)
        info_values.append(info_val)

    return dict(zip(info_keys, info_values))
